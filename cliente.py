import time
import os
from xmlrpc.client import ServerProxy
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Lista de IPs/portas dos outros nós na rede
PEERS = [
    'http://192.168.0.147:8084',
]

class Watcher:
    def __init__(self):
        self.DIRECTORY_TO_WATCH = os.getcwd()  # Diretório atual
        self.observer = Observer()
        self.processed_files = set()  # Conjunto de arquivos processados

    def run(self):
        event_handler = Handler(self.processed_files)
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(1)  
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()

class Handler(FileSystemEventHandler):
    def __init__(self, processed_files):
        super().__init__()
        self.clients = [ServerProxy(peer) for peer in PEERS]
        self.processed_files = processed_files

    def propagate_change(self, file_name, content, action):
        for client in self.clients:
            try:
                client.handle_package(file_name, content, action)
            except Exception as e:
                print(f"Erro ao comunicar com peer: {e}")

    def on_created(self, event):
        if not event.is_directory:
            file_name = event.src_path
            base_name = os.path.basename(file_name)
            
            if not base_name.startswith("1"):  # Evitar reação a arquivos do servidor
                print(f"{base_name} foi criado localmente.")
                with open(file_name, 'rb') as file:
                    content = file.read()
                self.propagate_change(base_name, content, "Created")
                self.processed_files.add(base_name)

    def on_modified(self, event):
        if not event.is_directory:
            file_name = event.src_path
            base_name = os.path.basename(file_name)
            
            if not base_name.startswith("1"):  # Evitar reação a arquivos do servidor
                print(f"{base_name} foi modificado localmente.")
                with open(file_name, 'rb') as file:
                    content = file.read()
                self.propagate_change(base_name, content, "Modified")

    def on_deleted(self, event):
        if not event.is_directory:
            file_name = event.src_path
            base_name = os.path.basename(file_name)
            
            if not base_name.startswith("1"):  # Evitar reação a arquivos do servidor
                print(f"{base_name} foi deletado localmente.")
                self.propagate_change(base_name, b'', "Deleted")
                self.processed_files.discard(base_name)

if __name__ == '__main__':
    print("Monitoramento Online em:", os.getcwd()) 
    w = Watcher()
    w.run()
