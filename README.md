# NYA

![Status](https://img.shields.io/badge/status-active%20development-black)
![Stars](https://img.shields.io/github/stars/senseyn/NYA?style=for-the-badge&color=yellow)
![Forks](https://img.shields.io/github/forks/senseyn/NYA?style=for-the-badge)
![Issues](https://img.shields.io/github/issues/senseyn/NYA?style=for-the-badge)
![Last Commit](https://img.shields.io/github/last-commit/senseyn/NYA)
![Repo Size](https://img.shields.io/github/repo-size/senseyn/NYA)

![Frontend](https://img.shields.io/badge/frontend-React-blue)
![Backend](https://img.shields.io/badge/backend-Node.js%20%7C%20FastAPI-green)
![Database](https://img.shields.io/badge/database-PostgreSQL-blueviolet)
![Streaming](https://img.shields.io/badge/streaming-HLS-orange)
![License](https://img.shields.io/badge/license-private-lightgrey)

> High-performance content streaming and catalog platform

---

## Overview

NYA - платформа потоковой доставки медиаконтента, совмещающая видеохостинг и каталог (картотеку).  
Проект ориентирован на стабильность, контроль инфраструктуры и масштабируемость под высокий онлайн.

Система предоставляет централизованный доступ к контенту без перегруженного интерфейса и внешних зависимостей.

---

## Core Features

- централизованный каталог контента  
- потоковое воспроизведение (HLS)  
- быстрый поиск и фильтрация  
- минималистичный интерфейс  
- управление медиаданными  
- масштабируемая backend-архитектура  

---

## Tech Stack

**Frontend**
- React  
- JavaScript  
- CSS Modules  

**Backend**
- Python  
- Node.js (Express)  
- FastAPI  
- JWT Authentication
- Redis + Celery

**Data Layer**
- PostgreSQL

**Media Pipeline**
- FFmpeg (HLS segmentation)  
- `.m3u8` playlists  
- `.ts` segments  

**Infrastructure**
- Docker  
- Nginx (reverse proxy + caching)  
- CDN (planned)  

---

## Architecture

```txt
Client (Browser)
        ↓
Frontend (React)
        ↓
API Layer (Node.js / FastAPI)
        ↓
---------------------------------
| PostgreSQL | Redis | Media FS |
---------------------------------
        ↓
Nginx (cache / proxy / HLS delivery)
```
---



[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=100&pause=1000&color=AC00F7&width=435&lines=%E2%AC%87+%D0%A7%D0%BC%D0%BE%D0%BD%D0%B8+300%25+%E2%AC%87)](https://git.io/typing-svg)

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/senseyn">
        <img src="https://github.com/senseyn.png" width="100px;" style="border-radius:50%;" alt="Seniorio Zog"/>
        <br />
        <sub><b>Seniorio Zog</b></sub>
      </a>
      <br />
      <sub>Frontend / Founder</sub>
    </td>
    <td align="center">
      <a href="https://github.com/FakeFu1ure">
        <img src="https://github.com/FakeFu1ure.png" width="100px;" style="border-radius:50%;" alt="FakeFu1ure"/>
        <br />
        <sub><b>FakeFu1ure</b></sub>
      </a>
      <br />
      <sub>Backend</sub>
    </td>
  </tr>
</table>

