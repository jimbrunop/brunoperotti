package dao;

import java.util.List;
import javax.persistence.EntityManager;
import javax.persistence.Query;
import dominio.Contato;

public class ContatoDaoJPA implements ContatoDao {

 private EntityManager em = null;
 
 public void setEm(EntityManager em) {
 this.em = em;
 }
 
 public void salvar(Contato x) {
 em.persist(x);
 }

 public void atualizar(Contato x) {
 x = em.merge(x);
 }

 public void deletar(Contato x) {
 em.remove(x);
 }

 public Contato buscaPorCodigo(int x) {
 return em.find(Contato.class, x);
 }

 @SuppressWarnings("unchecked")
 public List<Contato> buscaTodos() {
 String s = "SELECT u FROM " + Contato.class.getName() + " u ";
 Query query = em.createQuery(s);
 return query.getResultList();
 }
}
