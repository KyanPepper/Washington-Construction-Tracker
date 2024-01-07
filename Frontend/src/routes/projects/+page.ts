import type { PageLoad } from './$types';
export const load: PageLoad = async ({ fetch }) => {
  try {
    const response = await fetch('http://127.0.0.1:5000/getAll');
    if (!response.ok) {
      throw new Error(`Failed to fetch data: ${response.status}`);
    }
    const data = await response.json();
    return { allProjects: data };
  } catch (error) {
    console.error('Error fetching random projects during SSR:', error);
    return { allProjects: null };
  }
};
