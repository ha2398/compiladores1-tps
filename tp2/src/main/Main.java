package Main;

import java.io.*;
import lexer.*;
import parser.*;

public class Main {
	public static void Main(String[] args) throws IOException {
		Lexer lex = new Lexer();
		Parser parse = new Parser(lex);
		parse.program();
		System.out.println();
	}
}
