package com.example.loothelper;

import java.util.List;

import android.app.Activity;
import android.app.AlertDialog;
import android.content.DialogInterface;
import android.content.Intent;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.Toast;

public class ListarLootActivity extends Activity {

    ListView lvlLoot;
    LootBD lootBD;
    ArrayAdapter<Loot> adapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_listar_loot);

        lootBD = new LootBD(this);
        lvlLoot = (ListView) findViewById(R.id.listViewLoots);

        listarLoot();
        createListener();
    }

    @Override
    protected void onRestart() {
    	listarLoot();

        super.onRestart();
    }

    @Override
    protected void onRestoreInstanceState(Bundle savedInstanceState) {
    	listarLoot();
        super.onRestoreInstanceState(savedInstanceState);
    }


    public void sair(View view) {
        this.finish();
    }

    private void listarLoot() {
        List<Loot> loots = lootBD.getAll();

        adapter = new ArrayAdapter<Loot>(this, android.R.layout.simple_list_item_1, loots);

        lvlLoot = (ListView) findViewById(R.id.listViewLoots);
        lvlLoot.setAdapter(adapter);
    }


    private void createListener() {

        /*INICIO CLICK CURTO*/
    	lvlLoot.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id) {

                Intent intent = new Intent(ListarLootActivity.this, EditarLootActivity.class);
                intent.putExtra("loot", (Loot) lvlLoot.getItemAtPosition(position));
                startActivity(intent);
            }
        });
        /*FIM CLICK CURTO*/

        /*INICIO CLICK LONGO*/
        lvlLoot.setOnItemLongClickListener(new AdapterView.OnItemLongClickListener() {
            @Override
            public boolean onItemLongClick(AdapterView<?> parent, View view, int position, long id) {
                final Loot lootsSelecionados = (Loot) lvlLoot.getItemAtPosition(position);
                AlertDialog.Builder alerta = new AlertDialog.Builder(ListarLootActivity.this);
                alerta.setIcon(android.R.drawable.ic_delete);
                alerta.setTitle("Atenção");
                alerta.setMessage("Deseja Realmente remover o Loot " + lootsSelecionados.getItem());
                alerta.setNeutralButton("Não", null);
                alerta.setPositiveButton("Sim", new DialogInterface.OnClickListener() {
                    @Override
                    public void onClick(DialogInterface dialog, int which) {
                        if (lootBD.deletar(lootsSelecionados)) {
                            Toast.makeText(ListarLootActivity.this, "Deletado com sucesso", Toast.LENGTH_LONG).show();
                            listarLoot();
                        } else {
                            Toast.makeText(ListarLootActivity.this, "Não foi possivel remover", Toast.LENGTH_LONG).show();
                        }
                    }
                });
                alerta.show();
                return true;
            }
        });
        /*FIM CLICK LONGO*/


    }
}
