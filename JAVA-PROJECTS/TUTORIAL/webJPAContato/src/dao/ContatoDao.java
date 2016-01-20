package dao;

import java.util.List;
import dominio.Contato;

public interface ContatoDao {
 public void salvar(Contato x);
 public void atualizar(Contato x);
 public void deletar(Contato x);
 public Contato buscaPorCodigo(int x);
 public List<Contato> buscaTodos();
}