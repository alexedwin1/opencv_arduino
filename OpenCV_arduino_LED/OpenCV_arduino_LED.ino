/*
  Programa para Arduino: este programa enciende el LED 13 cuando
  se recibe el carácter 'h' por serial, y lo apaga si recibe otro.
 
*/
 
//Se define el pin del LED:
#define LED 13
 
//Variable para almacenar el caracter que llega por serial:
char lectura;
 
void setup()
{
   //Se inicia el Serial:
   Serial.begin(9600);
 
   //Definir el pin 13 como output:
   pinMode(LED, OUTPUT);
}
 
 
void loop()
{
   if(Serial.available() >= 1)
   {
      //Leemos el serial y guardamos el mensaje:
      lectura = Serial.read();
 
      //Si recibimos 'h', encendemos el LED:
      if(lectura == 'h')
      {
         digitalWrite(LED, HIGH);
      }
      //En caso contrario, lo apagamos:
      else
      {
         digitalWrite(LED, LOW);
      }
   }
}
