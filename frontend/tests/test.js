import { expect, test } from '@playwright/test';

test('index page has expected h1', async ({ page }) => {
	await page.goto('/');
	expect(await page.textContent('h1')).toBe('Willkommen bei parli.info, deinem Info-Portal zu aktuellen Themen aus dem österreichischen Parlament.');
});
