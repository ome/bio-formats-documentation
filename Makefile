all: html

html:
	mvn -DskipSphinxTests=true

linkcheck:
	mvn -DskipSphinxTests=false

clean:
	mvn clean
