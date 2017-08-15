package lexsyn;

import java_cup.runtime.Symbol;

%%
%cup
%%

"{" { return new Symbol(sym.LCBRACK); }
"}" { return new Symbol(sym.RCBRACK); }
";" { return new Symbol(sym.SEMI); }
"(" { return new Symbol(sym.LPAREN); }
")" { return new Symbol(sym.RPAREN); }

(int) { return new Symbol(sym.INTT); }
(char) { return new Symbol(sym.CHART); }
(bool) { return new Symbol(sym.BOOLT); }
(float) { return new Symbol(sym.FLOATT); }

"=" { return new Symbol(sym.ASSIGN); }

(while) { return new Symbol(sym.WHILE); }
(if) { return new Symbol(sym.IF); }
(else) { return new Symbol(sym.ELSE); }

[A-Za-z][A-Za-z0-9]* { return new Symbol(sym.ID); }

"<" { return new Symbol(sym.LT); }
"<=" { return new Symbol(sym.LE); }
">=" { return new Symbol(sym.GT); }
">" { return new Symbol(sym.GE); }

"+" { return new Symbol(sym.PLUS); }
"-" { return new Symbol(sym.MINUS); }

"*" { return new Symbol(sym.MUL); }
"/" { return new Symbol(sym.DIV); }

[+|-]?[0-9]*[.][0-9]+([E|e][+|-]?[0-9]+)? { return new Symbol(sym.REALN, new Double(yytext())); }
[+|-]?[0-9]+([E|e][+|-]?[0-9]+)? { return new Symbol(sym.INTN, new Integer(yytext())); }

[ \t\r\n\f] { /* ignore white space. */ }
. { System.err.println("Illegal character: "+yytext()); }