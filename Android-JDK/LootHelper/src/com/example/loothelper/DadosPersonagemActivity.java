package com.example.loothelper;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;

public class DadosPersonagemActivity extends  Activity {

    Loot loot;
    EditText editPersonagem, editLevel;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_dados_personagem);

        editPersonagem = (EditText) findViewById(R.id.editPersonagem);
        editLevel = (EditText) findViewById(R.id.editLevel);
      
        

        Bundle bundle = getIntent().getExtras();

        if (bundle != null) {
            loot = (Loot) bundle.getSerializable("loot");
            if(loot.getPersonagem() != null ){
                editPersonagem.setText(loot.getPersonagem());
            }
            if(loot.getLevel() != null){
                editLevel.setText(loot.getLevel());            	
            }
            
        } else {
            loot = new Loot();
        }

    }

    public void enviar(View v) {

        loot.setPersonagem(editPersonagem.getText().toString());
        loot.setLevel(editLevel.getText().toString());

        Intent intent = new Intent();
        intent.putExtra("loot", loot);

        setResult(10, intent);
        this.finish();

    }

}
