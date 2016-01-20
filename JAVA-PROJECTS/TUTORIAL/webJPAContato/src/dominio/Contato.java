package dominio;

import java.io.Serializable;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;

@Entity
public class Contato implements Serializable {

 private static final long serialVersionUID = 1L;

 @Id
 @GeneratedValue
 private Integer cod_contato;

 private String nome;
 private String telefone;
 private String email;

 public Integer getCod_contato() {
 return cod_contato;
 }
 public void setCod_contato(Integer cod_contato) {
 this.cod_contato = cod_contato;
 }
 public String getNome() {
 return nome;
 }
 public void setNome(String nome) {
 this.nome = nome;
 }
 public String getTelefone() {
 return telefone;
 }
 public void setTelefone(String telefone) {
 this.telefone = telefone;
 }
 public String getEmail() {
 return email;
 }
 public void setEmail(String email) {
 this.email = email;
 }
}

