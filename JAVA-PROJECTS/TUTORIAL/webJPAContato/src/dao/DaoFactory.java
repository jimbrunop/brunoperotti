package dao;

import javax.persistence.EntityManager;
import util.EMLocal;

public class DaoFactory {

 public static ContatoDao criarContatoDao() {
 ContatoDaoJPA aux = new ContatoDaoJPA();
 EntityManager em = EMLocal.getEntityManager();
 aux.setEm(em);
 return aux;
 }
}