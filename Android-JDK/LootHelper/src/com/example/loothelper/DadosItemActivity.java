package com.example.loothelper;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.EditText;

public class DadosItemActivity  extends Activity {

    Loot loot;
    EditText editItem, editTipo, editDano;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_dados_item);

        editItem = (EditText) findViewById(R.id.editItem);
        editTipo = (EditText) findViewById(R.id.editTipo);
        editDano = (EditText) findViewById(R.id.editDano);

        Bundle bundle = getIntent().getExtras();

        if (bundle != null) {
            loot = (Loot) bundle.getSerializable("loot");
            editItem.setText(loot.getItem());
            editTipo.setText(loot.getTipo());
            editDano.setText(loot.getDano());
        } else {
            loot = new Loot();
        }

    }

    public void enviar(View v) {

        loot.setItem(editItem.getText().toString());
        loot.setTipo(editTipo.getText().toString());
        loot.setDano(editDano.getText().toString());

        Intent intent = new Intent();
        intent.putExtra("loot", loot);

        setResult(11, intent);
        this.finish();


    }


}
