from routers.User import app as users
# from routers.products import app as products_router
# from routers.user import app as user_router
# from routers.user_profile import app as users_profile_router

from fastapi import APIRouter

app_router = APIRouter()
app_router.include_router(users)
# app_router.include_router(products_router)
# app_router.include_router(user_router)
# app_router.include_router(users_profile_router)