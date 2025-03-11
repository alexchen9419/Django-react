# 相機應用程式專案

一個全棧網頁應用程式，具有相機串流和圖像處理功能，使用 Django 後端、React 前端和 Docker 容器化技術構建。

## 創建者: alexchen9419
## 日期: 2025-03-08

## 📋 功能

- **Django 後端:**
  - 提供 GET、POST、PUT、DELETE 端點的 REST API
  - 通過端口轉發處理內部和外部請求
  - 相機串流功能
  - 實時灰度圖像處理
  - 整合 SQLite 資料庫

- **React 前端:**
  - 表單組件（輸入欄位、下拉選單、按鈕）
  - 相機串流顯示
  - 數據獲取和操作界面
  - 使用 Bootstrap 的響應式設計

- **Docker 整合:**
  - 完整的前端和後端容器化
  - 資料持久化的卷掛載
  - 通過 Docker Compose 進行容器編排

## 🔧 需求

- Docker 和 Docker Compose
- 系統連接的網絡攝像頭
- 開發環境: Python 3.9+，Node.js 16+

## 🚀 快速開始

### 使用 Docker（推薦）

1. 克隆此存儲庫:
   ```bash
   git clone https://github.com/alexchen9419/Django-react
   cd camera_app_project
   ```

2. 構建並啟動容器:
   ```bash
   cd docker
   docker-compose up --build
   ```

3. 訪問應用程式:
   - 前端: http://localhost
   - 後端 API: http://localhost/api/
   - 相機串流: http://localhost/camera/

### 手動開發設置

#### 後端設置:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Linux/Mac 或 venv\Scripts\activate 在 Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

#### 前端設置:
```bash
cd frontend
npm install
npm start
```

## 📖 使用指南

### API 端點

- **GET /api/internal-get/**: 測試內部 GET 請求
- **GET /api/external-get/**: 測試外部 GET 請求（通過端口轉發）
- **GET /api/items/**: 列出所有項目
- **POST /api/items/**: 創建新項目
- **GET /api/items/{id}/**: 獲取特定項目
- **PUT /api/items/{id}/**: 更新特定項目
- **DELETE /api/items/{id}/**: 刪除特定項目
- **GET /camera/**: 在瀏覽器中查看相機串流
- **GET /camera/grayscale/**: 查看灰度處理的相機串流

### 前端頁面

- **首頁**: 帶有 API 測試結果的儀表板
- **項目**: 資料庫項目的 CRUD 操作
- **相機視圖**: 實時相機串流，具有灰度處理選項

## 🏗️ 專案結構

```
camera_app_project/
├── backend/                # Django 後端
│   ├── api/                # API 應用
│   ├── camera_app/         # 主項目配置
│   ├── camera_stream/      # 相機串流應用
│   ├── db.sqlite3          # SQLite 資料庫
│   ├── manage.py
│   └── requirements.txt    # 後端依賴
├── frontend/               # React 前端
│   ├── public/
│   ├── src/
│   ├── package.json
│   └── ...
└── docker/                 # Docker 配置
    ├── Dockerfile.backend
    ├── Dockerfile.frontend
    ├── docker-compose.yml
    └── nginx.conf
```

## 🔍 主要實現細節

### 1. 相機串流
應用程式從連接的相機捕獲視頻，並使用多部分 HTTP 響應將其串流到瀏覽器。

### 2. 圖像處理
使用 OpenCV 實現簡單的圖像處理，將相機串流轉換為灰度圖像。

### 3. 資料庫操作
通過 API 和前端界面提供完整的 CRUD 操作。

### 4. 數據持久化
Docker 卷用於在容器重啟期間持久化 SQLite 資料庫。

## 🛠️ 使用技術

- **後端**: Django, Django REST framework, OpenCV
- **前端**: React, Axios, React Router, Bootstrap
- **資料庫**: SQLite
- **容器化**: Docker, Docker Compose
- **網頁伺服器**: Nginx（生產模式）

## ⚠️ 重要說明

1. **相機訪問**: 確保您的用戶或 Docker 有權訪問相機設備 (/dev/video0)。
2. **安全性**: 這是一個演示設置。對於生產環境，請實施適當的安全措施，如 HTTPS、限制 CORS 等。
3. **端口轉發**: 該設置通過將容器服務暴露給外部機器來演示端口轉發。

## 🤝 貢獻

1. Fork 此存儲庫
2. 創建您的功能分支 (`git checkout -b feature/amazing-feature`)
3. 提交您的更改 (`git commit -m 'Add some amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 打開 Pull Request

## 📄 授權

此專案根據 MIT 許可證授權 - 詳情請參閱 LICENSE 文件。
