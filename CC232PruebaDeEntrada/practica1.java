


class Persona{
	private int edad;
	private String nombre;
	private boolean genero;

public Persona(edad,nombre, genero){
	this.edad=edad;
	this.nombre=nombre;
	this.genero=genero;
}

public void setearEdad(edad){
	this.edad=edad;	
}

public void setearNombre(nombre){
	this.nombre=nombre;	
}

public String ObtenerNombre(){
	return nombre;
}

public int ObtenerEdad(){
	return edad;
}

public int calcularEdadPromedio(){
	total=0;
	i=0;
	for(Persona Grupo:Persona)
		total=total+Persona.edad;
		i=i+1;

	return	total/i;	
}

	public static void main(String[] args){
	
	Persona persona1,persona2,persona3;
	persona1= new Persona(17,"nombre1",0);
	persona2= new Persona(18,"nombre2",1);
	persona3= new Persona(19,"nombre3",1);	

	Persona.calcularEdadPromedio();
	}
} 
