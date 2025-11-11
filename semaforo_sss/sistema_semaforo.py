import serial
import time

PORTA_SERIAL = 'COM3'
BAUD_RATE = 9600
DISTANCIA_DETECCAO = 30
TEMPO_VERDE = 10
TEMPO_AMARELO = 3
TEMPO_SEGURANCA = 2

class Semaforo:
    def __init__(self, arduino):
        self.arduino = arduino
        print("🚦 Sistema iniciado")
        time.sleep(2)
        
    def apagar_todos(self):
        self.arduino.write(b'X')
        time.sleep(0.05)
        
    def led_a_vermelho(self):
        self.arduino.write(b'L')
        time.sleep(0.05)
        self.arduino.write(b'1')
        time.sleep(0.05)
        
    def led_a_amarelo(self):
        self.arduino.write(b'L')
        time.sleep(0.05)
        self.arduino.write(b'2')
        time.sleep(0.05)
        
    def led_a_verde(self):
        self.arduino.write(b'L')
        time.sleep(0.05)
        self.arduino.write(b'3')
        time.sleep(0.05)
        
    def led_b_vermelho(self):
        self.arduino.write(b'M')
        time.sleep(0.05)
        self.arduino.write(b'4')
        time.sleep(0.05)
        
    def led_b_amarelo(self):
        self.arduino.write(b'M')
        time.sleep(0.05)
        self.arduino.write(b'5')
        time.sleep(0.05)
        
    def led_b_verde(self):
        self.arduino.write(b'M')
        time.sleep(0.05)
        self.arduino.write(b'6')
        time.sleep(0.05)
        
    def ler_sensores(self):
        self.arduino.write(b'S')
        time.sleep(0.1)
        if self.arduino.in_waiting > 0:
            linha = self.arduino.readline().decode('utf-8').strip()
            try:
                partes = linha.split(',')
                dist_a = int(partes[0])
                dist_b = int(partes[1])
                return dist_a, dist_b
            except:
                return 999, 999
        return 999, 999
    
    def a_verde_b_vermelho(self):
        self.apagar_todos()
        self.led_a_verde()
        self.led_b_vermelho()
        print("A verde | B vermelho")
        
    def a_amarelo_b_vermelho(self):
        self.apagar_todos()
        self.led_a_amarelo()
        self.led_b_vermelho()
        print(" A amarelo |  B vermelho")
        
    def b_verde_a_vermelho(self):
        self.apagar_todos()
        self.led_b_verde()
        self.led_a_vermelho()
        print(" A vermelho |  B verde")
        
    def b_amarelo_a_vermelho(self):
        self.apagar_todos()
        self.led_b_amarelo()
        self.led_a_vermelho()
        print("🔴 A vermelho | 🟡 B amarelo")
        
    def ambos_vermelho(self):
        self.apagar_todos()
        self.led_a_vermelho()
        self.led_b_vermelho()
        print("🔴 A vermelho | 🔴 B vermelho")
        
    def esperar_monitorando(self, tempo, verde_em):
        inicio = time.time()
        while time.time() - inicio < tempo:
            dist_a, dist_b = self.ler_sensores()
            
            if verde_em == "A" and dist_b < DISTANCIA_DETECCAO:
                print(f"\n Veículo em B detectado ({dist_b}cm)!")
                self.interromper_para_b()
                return
                
            if verde_em == "B" and dist_a < DISTANCIA_DETECCAO:
                print(f"\n Veículo em A detectado ({dist_a}cm)!")
                self.interromper_para_a()
                return
                
            time.sleep(0.1)
    
    def interromper_para_a(self):
        print("🚨 Interrompendo para atender A")
        self.b_amarelo_a_vermelho()
        time.sleep(TEMPO_AMARELO)
        self.ambos_vermelho()
        time.sleep(TEMPO_SEGURANCA)
        self.a_verde_b_vermelho()
        time.sleep(TEMPO_VERDE)
        self.a_amarelo_b_vermelho()
        time.sleep(TEMPO_AMARELO)
        print("✅ Veículo atendido\n")
        
    def interromper_para_b(self):
        print("🚨 Interrompendo para atender B")
        self.a_amarelo_b_vermelho()
        time.sleep(TEMPO_AMARELO)
        self.ambos_vermelho()
        time.sleep(TEMPO_SEGURANCA)
        self.b_verde_a_vermelho()
        time.sleep(TEMPO_VERDE)
        self.b_amarelo_a_vermelho()
        time.sleep(TEMPO_AMARELO)
        print("✅ Veículo atendido\n")
    
    def ciclo_normal(self):
        print("\n" + "="*50)
        print("🔄 Ciclo normal")
        print("="*50)
        
        self.a_verde_b_vermelho()
        self.esperar_monitorando(TEMPO_VERDE, "A")
        
        self.a_amarelo_b_vermelho()
        time.sleep(TEMPO_AMARELO)
        
        self.ambos_vermelho()
        time.sleep(TEMPO_SEGURANCA)
        
        self.b_verde_a_vermelho()
        self.esperar_monitorando(TEMPO_VERDE, "B")
        
        self.b_amarelo_a_vermelho()
        time.sleep(TEMPO_AMARELO)
        
        self.ambos_vermelho()
        time.sleep(TEMPO_SEGURANCA)
    
    def executar(self):
        print("\n🟢 Sistema ativo! Ctrl+C para parar\n")
        try:
            while True:
                self.ciclo_normal()
        except KeyboardInterrupt:
            print("\n\n🛑 Encerrando")
            self.ambos_vermelho()
            self.arduino.close()
            print("👋 Finalizado")