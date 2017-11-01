Quadruplas::Quadruplas()
{
	quadruplas.resize(0);
}

Quadrupla Quadruplas::getQuadrupla( int pos )
{
	return quadruplas[pos];
}

void Quadruplas::addQuadrupla( Quadrupla q )
{
	quadruplas.push_back(q);
}

int Quadruplas::getNumQuadruplas()
{
	return quadruplas.size();
}

void Quadruplas::imprimeQuadruplas()
{
	Quadrupla p;
	cout << "Impressao das quadruplas" << endl;
	cout << "---------------------" << endl;
	for ( unsigned int i = 0; i < quadruplas.size(); i++ )
	{
		q = quadruplas[i];
		q.imprimeQuadrupla();
	}
	cout << "---------------------" << endl << endl;
}
