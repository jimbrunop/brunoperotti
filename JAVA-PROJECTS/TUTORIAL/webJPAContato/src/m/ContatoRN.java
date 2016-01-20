
package m;

import java.util.List;
import dao.ContatoDao;
import dao.DaoFactory;
import dominio.Contato;

public class ContatoRN {
 
 private ContatoDao dao;
 
 public ContatoRN() {
 dao = DaoFactory.criarContatoDao();
 }
 
 public List<Contato> buscarTodos() {
 return dao.buscaTodos();
 }
}