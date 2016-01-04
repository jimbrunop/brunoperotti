package com.example.loothelper;

import java.io.Serializable;

import android.content.ContentValues;

public class Loot implements Serializable{

	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	private int id;
	private String item;
	private String tipo;
	private String dano;
	private String personagem;
	private String level;
	
	
	public Loot(int id, String item, String tipo, String dano,
			String personagem, String level) {
		super();
		this.id = id;
		this.item = item;
		this.tipo = tipo;
		this.dano = dano;
		this.personagem = personagem;
		this.level = level;
	}
	
	public Loot( String item, String tipo, String dano,
			String personagem, String level) {
		super();
		
		this.item = item;
		this.tipo = tipo;
		this.dano = dano;
		this.personagem = personagem;
		this.level = level;
	}
	
	 public Loot() {
		// TODO Auto-generated constructor stub
	}

	public boolean hasAllAttributes() {
	        return (this.item != null && this.tipo != null && this.dano != null && this.personagem != null);
	    }

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getItem() {
		return item;
	}

	public void setItem(String item) {
		this.item = item;
	}

	public String getTipo() {
		return tipo;
	}

	public void setTipo(String tipo) {
		this.tipo = tipo;
	}

	public String getDano() {
		return dano;
	}

	public void setDano(String dano) {
		this.dano = dano;
	}

	public String getPersonagem() {
		return personagem;
	}

	public void setPersonagem(String personagem) {
		this.personagem = personagem;
	}

	public String getLevel() {
		return level;
	}

	public void setLevel(String level) {
		this.level = level;
	}
	 
	 
	 @Override
	    public String toString() {
	        return this.item + "-" + this.personagem;
	    }
	
	
	public ContentValues getContentValues() {

        ContentValues contentValues = new ContentValues();
        contentValues.put("item", this.item);
        contentValues.put("tipo", this.tipo);
        contentValues.put("dano", this.dano);
        contentValues.put("personagem", this.personagem);
        contentValues.put("level", this.level);

        return contentValues;
    }
	
	
	
	
}
