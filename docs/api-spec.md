# API Specification

## POST /v1/query

Submit enterprise RAG query.

### Request

```json
{
  "query": "What is our refund policy?",
  "conversation_id": "abc123"
}