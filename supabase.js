// Supabase client setup
// Replace with your own Supabase project URL and anon key
const SUPABASE_URL = 'https://kvguselfqoiesdjgoztt.supabase.co';
const SUPABASE_ANON_KEY = 'sb_publishable_DD3He-Mvvbtk4bGTUVCtYw_1DB7Dde6';

const supabase = window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);

// Export for use in index.html
window.supabaseClient = supabase;
