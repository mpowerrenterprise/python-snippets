import threading

class TheMesseanger(threading.Thread):
	def run(self):
		for _ in range(10): #_ means no variable.
			print(threading.currentThread().getName())


x=TheMesseanger(name="send");
y=TheMesseanger(name="receive");

x.start();
y.start();
