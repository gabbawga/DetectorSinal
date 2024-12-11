import smbus
import time
import smbus
from datetime import datetime 

MCP23017_ADDRESS = 0x21


IODIRA = 0x00  
IODIRB = 0x01  
GPIOA = 0x12   
GPIOB = 0x13   


bus = smbus.SMBus(1)  


bus.write_byte_data(MCP23017_ADDRESS, IODIRA, 0xFF)  
bus.write_byte_data(MCP23017_ADDRESS, IODIRB, 0xFF)  

while True:

    inputA = bus.read_byte_data(MCP23017_ADDRESS, GPIOA)
    inputB = bus.read_byte_data(MCP23017_ADDRESS, GPIOB)

    #for i in range(8):  
        #if (inputA & (1 << i)) == 0: 
            #print(f"Pulso detectado no pino {i} da Porta A!")
    
    for i in range(6):
        if (inputB & (1 << i)) == 0:
            timestamp = time.time()
            formatted_time = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
            print(f"Pulso no pino {i} no momento {formatted_time}")
        
    time.sleep(1)  
