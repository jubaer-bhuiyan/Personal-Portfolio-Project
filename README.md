# Personal Portfolio Project

A modern, responsive personal portfolio and blog web application built with Django.

---

## 🚀 Features

- **Personal Portfolio Home**: Showcase your profile, skills, and featured projects with images and descriptions.
- **Blog Section**: Write, publish, and display blog posts with formatted content and publication dates.
- **Responsive Design**: Clean, professional UI that looks great on desktop and mobile.
- **Media & Static Files**: Easily manage images, PDFs, and other assets.
- **Admin Panel**: Full Django admin for managing portfolio projects and blog posts.

---

## 📁 Project Structure

```
personalPortfolioProject/
├── blog/                # Blog app (models, views, templates)
│   └── templates/blog/  # Blog templates (allBlogs.html, detail.html)
├── media/               # Uploaded media files (images, etc.)
├── personalPortfolio/   # Main Django project settings and URLs
├── portfolio/           # Portfolio app (models, views, templates, static)
│   ├── static/portfolio/    # Static files (CSS, images, PDF)
│   └── templates/portfolio/ # Portfolio templates (base.html, home.html)
├── db.sqlite3           # SQLite database
├── manage.py            # Django management script
```

---

## 🖥️ Quick Start

1. **Clone the repository**
   ```powershell
   git clone <your-repo-url>
   cd personalPortfolioProject
   ```

2. **Install dependencies**
   (Recommended: use a virtual environment)
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   pip install django
   ```

3. **Apply migrations**
   ```powershell
   python manage.py migrate
   ```

4. **Create a superuser (for admin access)**
   ```powershell
   python manage.py createsuperuser
   ```

5. **Run the development server**
   ```powershell
   python manage.py runserver
   ```

6. **Access the site**
   - Portfolio: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   - Blog: [http://127.0.0.1:8000/blog/](http://127.0.0.1:8000/blog/)
   - Admin: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 📝 Customization

- **Profile Picture**: Replace `portfolio/static/portfolio/JubaerPP.png` with your own image.
- **Resume**: Update `portfolio/static/portfolio/JubaerCV.pdf`.
- **Projects**: Add/edit projects via the Django admin or by updating the database.
- **Blog Posts**: Add/edit blog posts via the Django admin.
- **Styling**: Modify `portfolio/static/portfolio/custom.css` for custom styles.

---

## 📦 Tech Stack

- **Backend**: Django 4.x
- **Frontend**: Bootstrap 4, custom CSS
- **Database**: SQLite (default, easy to switch)

---

## 📄 License

This project is open source and free to use for personal and educational purposes.

---

## 🙏 Credits

- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)
- [Font: Lato](https://fonts.google.com/specimen/Lato)

---

> Designed and developed by Jubaer Ahamed Bhuiyan
