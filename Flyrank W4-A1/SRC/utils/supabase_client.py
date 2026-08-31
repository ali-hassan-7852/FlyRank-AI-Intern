from supabase import create_client
from SRC.utils.settings import setting

supabase = create_client(setting.SUPABASE_URL, setting.SUPABASE_KEY)