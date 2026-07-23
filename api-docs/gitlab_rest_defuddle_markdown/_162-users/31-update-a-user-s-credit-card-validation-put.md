# 31-Update a user's credit_card_validation [PUT]

`PUT /api/v4/user/{user_id}/credit_card_validation`

Deprecated in 17.7

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | The ID or username of the user |

### Request Body (application/json)

```json
{
  "credit_card_validated_at": string (required), // The time when the user's credit card was validated
  "credit_card_expiration_month": integer (required), // The month the credit card expires
  "credit_card_expiration_year": integer (required), // The year the credit card expires
  "credit_card_holder_name": string (required), // The credit card holder name
  "credit_card_mask_number": string (required), // The last 4 digits of credit card number
  "credit_card_type": string (required), // The credit card network name
  "zuora_payment_method_xid": string, // The Zuora payment method ID
  "stripe_setup_intent_xid": string, // The Stripe setup intent ID
  "stripe_payment_method_xid": string, // The Stripe payment method ID
  "stripe_card_fingerprint": string, // The Stripe credit card fingerprint
}
```
### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "user_id": string,
  "credit_card_validated_at": string,
}
```

#### 400 - Bad Request

#### 404 - Not Found

