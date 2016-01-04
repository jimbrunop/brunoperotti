package com.example.loothelper;

import java.util.ArrayList;
import java.util.List;

import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;

public class LootBD {

   
    private Cursor cursor;

    
    private SQLiteDatabase banco;

   
    private static final String BANCO_NOME = "LootBanco.db";
    private static final int BANCO_ACESSO = 0;
    private static final String SQL_CRIACAO_TABELA =
            "CREATE TABLE IF NOT EXISTS loot(" +
                    " id integer not null primary key autoincrement," +
                    " item varchar(45) not null," +
                    " dano varchar(15) not null," +
                    " level varchar(150) not null, " +
                    " personagem varchar(15) not null, " +
                    " tipo varchar(15) not null)";

   
    private static final String SQL_SELECT_ALL = "SELECT id, item, dano, " +
            "level, personagem, tipo FROM  loot ORDER BY id Desc";

  
    public LootBD(Context context) {
        this.banco = context.openOrCreateDatabase(BANCO_NOME, BANCO_ACESSO, null);
        this.banco.execSQL(SQL_CRIACAO_TABELA);
    }

    
    public boolean inserir(Loot loot) {
        long res = -1;

        if (loot.getId() <= 0) {
            res = this.banco.insert("loot", null, loot.getContentValues());
        } else {
            String[] argumentos = new String[]{String.valueOf(loot.getId())};
            res = this.banco.update("loot", loot.getContentValues(), "id = ?", argumentos);
        }
        return res != -1;
    }

   
    public boolean deletar(Loot loot) {
        return this.banco.delete("loot", "id=? ", new String[]{String.valueOf(loot.getId())}) != -1;
    }

    
    public List<Loot> getAll() {
        List<Loot> loots = new ArrayList<Loot>();

        this.cursor = this.banco.rawQuery(SQL_SELECT_ALL, null);

        while (this.cursor.moveToNext()) {
            loots.add(new Loot(
                    cursor.getInt(cursor.getColumnIndex("id")),
                    cursor.getString(cursor.getColumnIndex("item")),
                    cursor.getString(cursor.getColumnIndex("tipo")),
                    cursor.getString(cursor.getColumnIndex("dano")),
                    cursor.getString(cursor.getColumnIndex("personagem")),
                    cursor.getString(cursor.getColumnIndex("level"))
            ));
        }
        return loots;
    }
}