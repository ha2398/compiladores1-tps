class Quadrupla
{
	private:
		string op; /* operador */
		string ops[NUM_OPERANDOS]; /* operandos 0, 1 e 2 */
	public:
		Quadrupla(); /* construtor */
		Quadrupla( string op, string a, string b, string c); /* construtor */
		string get-operador( void ); /* retorna operador */
		void set-operador( string novo ); /* muda operador para novo */
		string get-operado-pos( int pos ); /* retorna operando pos */
		void set-ops( int pos, string v ); /* muda valor do operando pos para v */
		Quadrupla stringToQuadrupla( string s ); /* retorna a quadrupla representada por s */
		void imprimeQuadrupla();
};
