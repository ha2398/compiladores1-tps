package lexsyn;

import java_cup.runtime.Symbol;

%%
%cup
%%

[ \t\r\n\f] { /* ignore white space. */
	System.out.print(yytext());
}

"{" {
	System.out.print(yytext());
	return new Symbol(sym.LCBRACK);
}

"}" {
	System.out.print(yytext());
	return new Symbol(sym.RCBRACK);
}

";" {
	System.out.print(yytext());
	return new Symbol(sym.SEMI);
}

"(" {
	System.out.print(yytext());
	return new Symbol(sym.LPAREN);
}

")" {
	System.out.print(yytext());
	return new Symbol(sym.RPAREN);
}

(int) {
	System.out.print(yytext());
	return new Symbol(sym.INTT);
}

(char) {
	System.out.print(yytext());
	return new Symbol(sym.CHART);
}

(bool) {
	System.out.print(yytext());
	return new Symbol(sym.BOOLT);
}

(float) {
	System.out.print(yytext());
	return new Symbol(sym.FLOATT);
}

"=" {
	System.out.print(yytext());
	return new Symbol(sym.ASSIGN);
}

(while) {
	System.out.print(yytext());
	return new Symbol(sym.WHILE);
}

(if) {
	System.out.print(yytext());
	return new Symbol(sym.IF);
}

(else) {
	return new Symbol(sym.ELSE);
}

[A-Za-z][A-Za-z0-9]* {
	System.out.print(yytext());
	return new Symbol(sym.ID);
}

"<" {
	System.out.print(yytext());
	return new Symbol(sym.LT);
}

"<=" {
	System.out.print(yytext());
	return new Symbol(sym.LE);
}

">=" {
	System.out.print(yytext());
	return new Symbol(sym.GE);
}

">" {
	System.out.print(yytext());
	return new Symbol(sym.GT);
}

"+" {
	System.out.print(yytext());
	return new Symbol(sym.PLUS);
}

"-" {
	System.out.print(yytext());
	return new Symbol(sym.MINUS);
}

"*" {
	System.out.print(yytext());
	return new Symbol(sym.MUL);
}

"/" {
	System.out.print(yytext());
	return new Symbol(sym.DIV);
}

[+|-]?[0-9]*[.][0-9]+([E|e][+|-]?[0-9]+)? {
	System.out.print(yytext());
	return new Symbol(sym.REALN, new Double(yytext()));
}

[+|-]?[0-9]+([E|e][+|-]?[0-9]+)? {
	System.out.print(yytext());
	return new Symbol(sym.INTN, new Integer(yytext()));
}

. {
	System.out.println("\n\n[ERROR] Illegal character: "+yytext());
	System.exit(1);
}