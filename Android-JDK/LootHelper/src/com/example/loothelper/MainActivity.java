package com.example.loothelper;

import android.app.Activity;
import android.app.AlertDialog;
import android.content.Intent;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;

public class MainActivity extends Activity {

    Loot loot;
    LootBD lootBD;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        loot = new Loot();
        lootBD = new LootBD(this);
    }

    public void eventoButton(View v) {
        Intent intent = null;

        switch (v.getId()) {

            case R.id.btnMenuItem:
                intent = new Intent(this, DadosItemActivity.class);
                intent.putExtra("loot", loot);
                break;

            case R.id.btnMenuPersonagem:
                intent = new Intent(this, DadosPersonagemActivity.class);
                intent.putExtra("loot", loot);
                break;
                
        	case R.id.btnAbout:
    			intent = new Intent(this, AboutActivity.class);
    			
    		break;

        }

        if (intent != null) {
            startActivityForResult(intent, RESULT_FIRST_USER);
        }
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        Bundle param;

        switch (resultCode) {
            case 10:
                param = data.getExtras();
                loot = (Loot) param.getSerializable("loot");
                break;

            case 11:
                param = data.getExtras();
                loot = (Loot) param.getSerializable("loot");
                break;
        }
        super.onActivityResult(requestCode, resultCode, data);
    }

    public void cadastrarLoot(View view) {

        AlertDialog.Builder alerta = new AlertDialog.Builder(this);

        if (!loot.hasAllAttributes()) {
            alerta.setTitle("Alerta");
            alerta.setMessage("Não foram preenchidos todos os campos");
            alerta.setIcon(android.R.drawable.ic_dialog_alert);
            alerta.setNeutralButton("Fechar", null);
        } else {
            if (lootBD.inserir(loot)) {
                alerta.setTitle("Sucesso");
                alerta.setMessage("Cadastro efetuado com sucesso");
                alerta.setIcon(android.R.drawable.ic_dialog_info);
                alerta.setNeutralButton("Fechar", null);
                loot = new Loot();
            } else {
                alerta.setTitle("Alerta");
                alerta.setMessage("Não foi possivel cadastrar o contato, entre em contato com o suporte");
                alerta.setIcon(android.R.drawable.ic_dialog_alert);
                alerta.setNeutralButton("Fechar", null);
            }
        }
        alerta.show();
    }

    public void listarLoot(View view) {
        Intent intent = new Intent(this, ListarLootActivity.class);
        startActivity(intent);
    }

    public void sair(View view) {
        this.finish();
    }
}
