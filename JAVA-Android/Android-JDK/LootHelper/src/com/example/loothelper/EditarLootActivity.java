package com.example.loothelper;

import android.app.Activity;
import android.app.AlertDialog;
import android.content.DialogInterface;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.EditText;

public class EditarLootActivity extends Activity {

    Loot loot;
    LootBD lootBD;
    EditText editItem, editTipo, editDano, editPersonagem, editLvl;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_editar_loot);

        Bundle bundle = getIntent().getExtras();
        loot = (Loot) bundle.getSerializable("loot");

        editItem = (EditText) findViewById(R.id.editItem);
        editTipo = (EditText) findViewById(R.id.editTipo);
        editDano = (EditText) findViewById(R.id.editDano);
        editPersonagem = (EditText) findViewById(R.id.editPersonagem);
        editLvl = (EditText) findViewById(R.id.editLvl);

        editItem.setText(loot.getItem());
        editTipo.setText(loot.getTipo());
        editDano.setText(loot.getDano());
        editPersonagem.setText(loot.getPersonagem());
        editLvl.setText(loot.getLevel());

        lootBD = new LootBD(this);

    }

    public void editar(View view) {
        loot.setItem(editItem.getText().toString());
        loot.setTipo(editTipo.getText().toString());
        loot.setDano(editDano.getText().toString());
        loot.setPersonagem(editPersonagem.getText().toString());
        loot.setLevel(editLvl.getText().toString());

        AlertDialog.Builder alerta = new AlertDialog.Builder(EditarLootActivity.this);
        if (loot.hasAllAttributes()) {

            alerta.setTitle("Alerta");
            alerta.setMessage("Não foram preenchidos todos os campos");
            alerta.setIcon(android.R.drawable.ic_dialog_alert);
            alerta.setNeutralButton("Fechar", null);

            if (lootBD.inserir(loot)) {
                alerta.setTitle("Sucesso");
                alerta.setMessage("Loot Editado com sucesso");
                alerta.setNeutralButton("OK", new DialogInterface.OnClickListener() {
                    @Override
                    public void onClick(DialogInterface dialog, int which) {
                        EditarLootActivity.this.finish();
                    }
                });
                alerta.setIcon(android.R.drawable.ic_dialog_info);
            } else {
                alerta.setTitle("Erro");
                alerta.setMessage("Falhar ao editar o loot");
                alerta.setNeutralButton("Fechar", null);
                alerta.setIcon(android.R.drawable.ic_dialog_alert);
            }
        }


        alerta.show();
    }

}
