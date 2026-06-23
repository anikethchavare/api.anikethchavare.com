# api.anikethchavare.com / docs / 5_setup.md

This document provides step-by-step instructions on how to configure, run, and deploy the API application in a local environment.

<hr>

## 1. 💻 Local Setup & Deployment

Ensure you have **Python 3.10+** and a **PostgreSQL** database ready before proceeding.

1. **Download & Install:** Clone the repository via Git or download and extract the source ZIP file of the latest release.

    ```bash
    git clone https://github.com/anikethchavare/api.anikethchavare.com.git
    cd api.anikethchavare.com
    pip install -r requirements.txt uvicorn
    ```

2. **Environment Setup:** Add your `DATABASE_URL`, `UPSTASH_REDIS_URL`, `CRON_SECRET` to a `.env` file in the root directory. The `UPSTASH_REDIS_URL` is the URL of the Redis (Upstash) instance in Vercel. The `CRON_SECRET` can be anything you like, but must be kept a secret to ensure only Vercel Cron Jobs can purge the request logs.

    ```env
    DATABASE_URL=<YOUR_POSTGRESQL_DATABASE_URL>
    UPSTASH_REDIS_URL=<YOUR_UPSTASH_REDIS_CONNECTION_STRING>
    CRON_SECRET=<YOUR_VERCEL_CRON_SECRET>
    ```

3. **Launch:** Start the local development server.

    ```bash
    uvicorn server:app --reload
    ```

**Note:** For local development, setting `UPSTASH_REDIS_URL="memory://"` forces the application to track rate limits directly inside your local computer's volatile RAM.

<hr>

## 2. ⚡ Deploy to Vercel

Since the core engine is optimized for serverless environments, you can deploy it to Vercel using either the command line interface or the web dashboard.

### Option A: Via Vercel CLI (Terminal)

1. **Install Vercel CLI:** If you haven't already, install the utility globally via npm:

    ```bash
    npm install -g vercel
    ```

2. **Deploy & Link:** Open your terminal in the root directory and initialize the deployment process:

    ```bash
    vercel
    ```

Follow the terminal prompts to log in, create a new project, and link your repository.

3. **Set Environment Variables:** When prompted or after initialization, add your production database URL to your environment variables:

    ```bash
    vercel env add DATABASE_URL
    ```

### Option B: Via Vercel Dashboard (Browser)

1. **Push to Git:** Ensure your latest project changes are committed and pushed to your GitHub repository.
2. **Import Project:** Go to the [Vercel Dashboard](https://vercel.com), click **Add New...**, and select **Project**.
3. **Connect Repository:** Find and import your repository from your connected Git account.
4. **Configure Environment Variables:** Under the **Environment Variables** dropdown, add a new key named `DATABASE_URL` and paste your production PostgreSQL connection string as the value.
5. **Deploy:** Click **Deploy**. Vercel will automatically build and assign a production URL to your deployment.

<hr>

## 3. 🔧 Testing Architecture

The test suite utilizes a localized environment structure to run integration tests without needing live network access to production third-party resources.

* **Rate Limiting Isolation:** During `pytest` runs, the configuration hooks intercept external service requirements and mock/force `memory://` as the tracking backend. This prevents local development tests from consuming production Upstash service limits.
* **Database Mocking:** Testing workflows simulate isolated execution paths ensuring that tests do not clear or pollute the live Neon PostgreSQL database instance.

<hr>

## 4. 🧭 Next Guide

* **[v1/1_core.md](./v1/1_core.md) $\rightarrow$** Proceed to the **Version 1** core documentation to explore the primary API endpoints, request patterns, and integration workflows.