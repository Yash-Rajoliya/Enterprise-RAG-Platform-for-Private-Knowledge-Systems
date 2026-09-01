export class EnterpriseRAGClient {

  baseUrl: string;
  apiKey: string;

  constructor(
    baseUrl: string,
    apiKey: string
  ) {
    this.baseUrl = baseUrl;
    this.apiKey = apiKey;
  }

  async query(
    question: string,
    tenantId: string
  ) {

    const response = await fetch(
      `${this.baseUrl}/api/v1/query`,
      {
        method: "POST",

        headers: {
          "Content-Type":
          "application/json",

          "Authorization":
          `Bearer ${this.apiKey}`
        },

        body: JSON.stringify({
          query: question,
          tenant_id: tenantId
        })
      }
    );

    return await response.json();
  }

  async health() {

    const response = await fetch(
      `${this.baseUrl}/api/v1/health`
    );

    return await response.json();
  }
}