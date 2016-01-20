
<?xml version="1.0" encoding="ISO-8859-1" ?>
<%@page import="javax.persistence.EntityManager"%>
<%@page import="util.EMLocal"%>
<%@page import="dominio.Contato"%>
<%@page import="java.util.List"%>
<%@page import="m.ContatoRN"%>
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
<title>Exemplo de acesso a dados via web</title>
</head>
<body>
<h1>Exemplo web com BD (ainda sem MVC)</h1>
<hr/>
<h2>Listagem de Contatos</h2>
<%
 EntityManager em = EMLocal.getEntityManager();
 em.getTransaction().begin();

 ContatoRN contatoRN = new ContatoRN();
 List<Contato> lista = contatoRN.buscarTodos();

 em.getTransaction().commit();
 EMLocal.cleanEntityManager();
%>
 <table border="1">
 <tr>
 <td>Código</td>
 <td>Nome</td>
 <td>Telefone</td>
 <td>E-mail</td>
 </tr>
<% 
 for (Contato x : lista) {
%>
 <tr>
 <td><%=x.getCod_contato() %></td>
 <td><%=x.getNome() %></td>
 <td><%=x.getTelefone() %></td>
 <td><%=x.getEmail() %></td>
 </tr>
<%
 }
%>
 </table>
</body>
</html>
