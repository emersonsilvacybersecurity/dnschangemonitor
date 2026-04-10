# 🌐 Python DNS Change Monitor 

Ferramenta de monitoramento de infraestrutura que detecta alterações no IP de domínios, auxiliando na identificação de mudanças de ambiente ou possíveis ataques como DNS Hijacking.

---

## 🎯 Objetivo

Monitorar a resolução DNS de um domínio e alertar automaticamente quando houver mudança de IP, fornecendo visibilidade sobre alterações que podem impactar segurança, disponibilidade e integridade dos serviços.

---

## ⚙️ Funcionalidades

- 🔎 Resolução DNS automática (domínio → IP).
- 📡 Detecção de alteração de endereço IP.
- 🚨 Geração de alerta em tempo real quando ocorre mudança.
- 💾 Persistência de histórico em arquivo local.
- ⚠️ Tratamento de erros de resolução DNS.
- 🛡️ Apoio a atividades de SOC, Blue Team e Monitoramento de Infraestrutura.

---

## 🧰 Tecnologias Utilizadas

- Python 3.x  
- socket (resolução DNS)  
- os (manipulação de arquivos)  

---

## 🚀 Como executar

Siga os passos abaixo para rodar o projeto localmente:

### 📥 1. Clonar o repositório
```bash
git clone https://github.com/emersonsilvacybersecurity/dnschangemonitor.git
```

### 📂 2. Acessar a pasta do projeto
```bash
cd dnschangemonitor
```

### ▶️ 3. Executar o script

#### 💻 Windows
```bash
python dns_monitor.py
```

#### 🐧 Linux
```bash
python3 dns_monitor.py
```

---

## 🧠 Como funciona

O script resolve o domínio informado e compara o IP atual com o último IP registrado localmente:

- 🆕 Primeira execução → cria um arquivo com o IP atual  
- 🔄 IP alterado → gera alerta e atualiza o registro  
- ✅ Sem alteração → informa que o domínio permanece estável  

---

## 🌐 Contexto de segurança

O monitoramento de DNS é essencial porque mudanças inesperadas podem:

- 🚨 Indicar **DNS Hijacking**
- ⚠️ Causar indisponibilidade de serviços
- 🎯 Redirecionar tráfego para servidores maliciosos

Ferramentas profissionais de mercado utilizam esse mesmo conceito de comparação contínua para detectar alterações em registros DNS e alertar rapidamente equipes de segurança.

---

## ⚠️ Análise de segurança (Aviso Legal)

Este projeto foi desenvolvido exclusivamente para fins educacionais e auditorias de segurança autorizadas.

- ⚖️ Ética: O uso desta ferramenta deve ser restrito a ambientes autorizados.
- 🚫 Responsabilidade: O autor não se responsabiliza por qualquer uso indevido ou danos causados a terceiros.

---

