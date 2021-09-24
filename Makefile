test:
	gcc -g -o test main.c

clean:
	rm test

install:
	mkdir -p $(DESTDIR)/nik/bin
	install -m 0755 test $(DESTDIT)/nik/bin/test
