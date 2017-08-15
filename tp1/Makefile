all: lex cup

.PHONY: lex
lex:
	javac JLex/Main.java
	java JLex.Main *.lex
	mv *.lex.java Yylex.java

.PHONY: cup
cup:
	java -jar java_cup/java-cup-11b.jar -interface -parser parser *.cup
	javac -d . -cp java_cup/java-cup-11b-runtime.jar *.java	

.PHONY: run
run: all
	java -cp java_cup/java-cup-11b-runtime.jar:. lexsyn.parser

.PHONY: clean
clean:
	rm -f JLex/*.class *.lex.java
	rm -f *.java
	rm -rf lexsyn
