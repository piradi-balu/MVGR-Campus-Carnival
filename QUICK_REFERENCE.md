# Campus Carnival MVGR - Quick Reference

## URL Routes

### Public Routes (No Login Required)
- `GET /` → Home page with login/register modals
- `POST /login/` → Process login form
- `POST /register/` → Process registration form

### Protected Routes (Login Required)
- `GET /students/` → View all students and add new student form
- `POST /students/` → Add new student
- `GET /update/<id>/` → Edit student page
- `POST /update/<id>/` → Update student
- `GET /delete/<id>/` → Delete student
- `GET /logout/` → Logout user

## Modal Triggers

### Login Modal
- ID: `#loginModal`
- Trigger: Click "Login" button on home page
- Form ID: `#loginForm`
- Action: POST to `/login/`

### Register Modal
- ID: `#registerModal`
- Trigger: Click "Register" button on home page
- Form ID: `#registerForm`
- Action: POST to `/register/`

## Form Fields

### Login Form
- `username` (text, required)
- `password` (password, required)
- CSRF token

### Register Form
- `first_name` (text, required)
- `last_name` (text, required)
- `username` (text, required)
- `password` (password, required)
- CSRF token

### Add Student Form
- `name` (text, required)
- `description` (textarea, required)
- `photo` (file, optional)
- CSRF token

### Update Student Form
- `name` (text, required)
- `description` (textarea, required)
- `photo` (file, optional)
- CSRF token

## View Functions

### `home(request)`
- **Method**: GET, POST
- **Authentication**: None required
- **Functionality**: Displays home page with login/register modals
- **Redirects**: If authenticated → students page

### `Students(request)`
- **Method**: GET, POST
- **Authentication**: Required (@login_required)
- **Functionality**: Displays all students, allows adding new student
- **GET Parameters**: `search` (optional) - filters by name
- **Redirects**: On POST → students page

### `update_student(request, id)`
- **Method**: GET, POST
- **Authentication**: Required (@login_required)
- **Functionality**: Displays and processes student update form
- **Redirects**: On POST → students page

### `delete_student(request, id)`
- **Method**: GET (or POST with confirmation)
- **Authentication**: Required (@login_required)
- **Functionality**: Deletes student by ID
- **Redirects**: After deletion → students page

### `login_page(request)`
- **Method**: GET, POST
- **Authentication**: None required
- **Functionality**: Authenticates user credentials
- **Errors**: Shows messages for invalid username/password
- **Redirects**: On success → students page, On error → home page with modal

### `register(request)`
- **Method**: GET, POST
- **Authentication**: None required
- **Functionality**: Creates new user account
- **Errors**: Shows message for duplicate username
- **Redirects**: On success → home page with login modal, On error → home page with register modal

### `logout_page(request)`
- **Method**: GET
- **Authentication**: Required (implied)
- **Functionality**: Logs out current user
- **Redirects**: → home page

## Error Messages

### Login Errors
- "Invalid Username" - User doesn't exist
- "Invalid password" - Password doesn't match username

### Register Errors
- "Username already taken" - Username exists in database

### Success Messages
- "Account created successfully. Please login." - After successful registration

## CSS Classes (Styling)

### Navbar
- `.navbar` - Main navbar with gradient background
- `.navbar-brand` - Brand name in navbar
- `.user-greeting` - User welcome message
- `.btn-logout` - Logout button style

### Modals
- `.modal-header` - Modal header with gradient
- `.modal-body` - Modal body with form
- `.btn-close` - Close button with filter for visibility

### Buttons
- `.btn-login-custom` - Login button on home
- `.btn-register-custom` - Register button on home
- `.btn-logout` - Logout button in navbar

### Cards
- `.card` - Card container
- `.card-header` - Card header with gradient
- `.card-body` - Card body content

## Database Models

### User (Django Built-in)
- `id` - Primary key
- `username` - Unique username
- `password` - Hashed password
- `first_name` - First name
- `last_name` - Last name
- `email` - Email (optional)

### Student
- `id` - Primary key
- `user` - Foreign key to User (nullable)
- `name` - Student name
- `description` - Student description
- `photo` - Image field (upload_to="studentfolder")

## JavaScript Features

### Modal Switching
- Users can switch between login and register modals using links
- Modal state is maintained with data attributes

### Auto-Open Modals
- Login modal auto-opens if there's an error: `show_login_modal`
- Register modal auto-opens if there's an error: `show_register_modal`

## Common Issues & Solutions

### Modals not closing after submission
✅ Use `data-bs-dismiss="modal"` on close button
✅ Return page with context variables for error handling

### Users can access protected pages without login
✅ Use `@login_required(login_url='home')` decorator
✅ Check URL configuration in urls.py

### Redirects not working
✅ Use named routes: `redirect('students')` instead of `redirect('/')`
✅ Update all redirect statements to use route names

### Images not displaying
✅ Ensure `MEDIA_URL` and `MEDIA_ROOT` configured in settings.py
✅ Add media files serving in urls.py (for development)

## Browser Support
- Chrome/Edge (Latest)
- Firefox (Latest)
- Safari (Latest)
- Mobile browsers (Responsive design)

## Performance Notes
- Database queries optimized with `.get()`, `.filter()`
- Images stored in media folder
- Static files served by Django in development
- Session-based auth (not token-based)
