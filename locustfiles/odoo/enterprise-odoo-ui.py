from locust import HttpUser, task, SequentialTaskSet, constant

pheaders = {
    'API-KEY': 'efishery_123',
    'Cookie': 'session_id=e6656a8f00beb5bcc7468f4a9fb246400f20754d'
}


class SeqTaskEasyCase(SequentialTaskSet):
    @task
    def searchReadSaleOrder(self):
        sale_body = {
            "jsonrpc": "2.0",
            "method": "call",
            "params": {
                "args": [],
                "model": "sale.order",
                "method": "web_read_group",
                "kwargs": {
                    "context": {
                        "lang": "en_US",
                        "tz": "Asia/Jakarta",
                        "uid": 2,
                        "allowed_company_ids": [
                            4,
                            2,
                            3
                        ],
                        "search_default_my_quotation": 1
                    },
                    "domain": [],
                    "fields": [
                        "name",
                        "create_date",
                        "date_order",
                        "commitment_date",
                        "expected_date",
                        "x_point",
                        "payment_term_id",
                        "partner_id",
                        "user_id",
                        "activity_ids",
                        "activity_exception_decoration",
                        "activity_exception_icon",
                        "activity_state",
                        "activity_summary",
                        "activity_type_id",
                        "activity_type_icon",
                        "team_id",
                        "tag_ids",
                        "warehouse_id",
                        "company_id",
                        "amount_untaxed",
                        "amount_tax",
                        "amount_total",
                        "state",
                        "invoice_status",
                        "message_needaction",
                        "currency_id"
                    ],
                    "groupby": [
                        "x_point",
                        "payment_term_id"
                    ],
                    "limit": 80,
                    "orderby": "",
                    "lazy": True
                }
            },
            "id": 879348961
        }
        self.client.post(
            "/web/dataset/call_kw/sale.order/web_read_group?model=sale.order",
            headers=pheaders,
            json=sale_body
        )

    @task
    def searchReadPurchaseOrder(self):
        purchase_body = {
            "jsonrpc": "2.0",
            "method": "call",
            "params": {
                "model": "purchase.order",
                "domain": [],
                "fields": [
                    "priority",
                    "message_unread",
                    "partner_ref",
                    "name",
                    "date_approve",
                    "partner_id",
                    "company_id",
                    "date_planned",
                    "user_id",
                    "date_order",
                    "activity_ids",
                    "activity_exception_decoration",
                    "activity_exception_icon",
                    "activity_state",
                    "activity_summary",
                    "activity_type_id",
                    "activity_type_icon",
                    "origin",
                    "amount_untaxed",
                    "amount_total",
                    "currency_id",
                    "state",
                    "invoice_status"
                ],
                "limit": 80,
                "sort": "",
                "context": {
                    "lang": "en_US",
                    "tz": "Asia/Jakarta",
                    "uid": 2,
                    "allowed_company_ids": [
                        4,
                        2,
                        3
                    ],
                    "quotation_only": True,
                    "bin_size": True
                }
            },
            "id": 406012263
        }
        self.client.post(
            "/web/dataset/search_read?model=purchase.order",
            headers=pheaders,
            json=purchase_body
        )

    @task
    def searchReadRentalOrder(self):
        rental_body = {
            "jsonrpc": "2.0",
            "method": "call",
            "params": {
                "model": "sale.order",
                "domain": [],
                "fields": [
                    "name",
                    "partner_id",
                    "amount_total",
                    "date_order",
                    "state",
                    "next_action_date",
                    "has_late_lines",
                    "currency_id",
                    "activity_state",
                    "rental_status",
                    "install_status"
                ],
                "limit": 80,
                "sort": "",
                "context": {
                    "lang": "en_US",
                    "tz": "Asia/Jakarta",
                    "uid": 2,
                    "allowed_company_ids": [
                        4,
                        2,
                        3
                    ],
                    "params": {
                        "action": 500,
                        "cids": "4,2,3",
                        "menu_id": 319,
                        "model": "sale.order",
                        "view_type": "kanban"
                    },
                    "default_is_rental_order": 1,
                    "search_default_from_rental": 1,
                    "bin_size": True
                }
            },
            "id": 607040815
        }
        self.client.post(
            "/web/dataset/search_read?model=sale.order&type=rental",
            headers=pheaders,
            json=rental_body
        )

    @task
    def searchReadResPartner(self):
        partner_body = {
            "jsonrpc": "2.0",
            "method": "call",
            "params": {
                "model": "res.partner",
                "domain": [],
                "fields": [
                    "id",
                    "color",
                    "display_name",
                    "title",
                    "email",
                    "parent_id",
                    "is_company",
                    "function",
                    "phone",
                    "street",
                    "street2",
                    "zip",
                    "city",
                    "country_id",
                    "mobile",
                    "sale_order_count",
                    "purchase_order_count",
                    "state_id",
                    "category_id",
                    "image_128",
                    "type",
                    "activity_state",
                    "code",
                    "activity_ids",
                    "activity_exception_decoration",
                    "activity_exception_icon"
                ],
                "limit": 80,
                "sort": "",
                "context": {
                    "lang": "en_US",
                    "tz": "Asia/Jakarta",
                    "uid": 2,
                    "allowed_company_ids": [
                        4,
                        2,
                        3
                    ],
                    "default_is_company": True,
                    "bin_size": True
                }
            },
            "id": 246636276
        }
        self.client.post(
            "/web/dataset/search_read?model=res.partner",
            headers=pheaders,
            json=partner_body
        )


class SeqTaskHardCase(SequentialTaskSet):

    @task
    def searchReadInvoiceOdooUI(self):
        invoice_body = {
            "jsonrpc": "2.0",
            "method": "call",
            "params": {
                "model": "account.move",
                "domain": [
                    [
                        "move_type",
                        "=",
                        "out_invoice"
                    ]
                ],
                "fields": [
                    "name",
                    "create_uid",
                    "partner_id",
                    "invoice_source_email",
                    "invoice_partner_display_name",
                    "invoice_date",
                    "invoice_date_due",
                    "date",
                    "invoice_origin",
                    "payment_reference",
                    "ref",
                    "invoice_user_id",
                    "l10n_id_tax_number",
                    "l10n_id_csv_created",
                    "team_id",
                    "activity_ids",
                    "activity_exception_decoration",
                    "activity_exception_icon",
                    "activity_state",
                    "activity_summary",
                    "activity_type_id",
                    "activity_type_icon",
                    "company_id",
                    "amount_untaxed_signed",
                    "amount_tax_signed",
                    "amount_total_signed",
                    "amount_residual_signed",
                    "currency_id",
                    "company_currency_id",
                    "state",
                    "posted_date",
                    "register_payment_date",
                    "is_generate",
                    "payment_state",
                    "move_type"
                ],
                "limit": 80,
                "sort": "",
                "context": {
                    "lang": "en_US",
                    "tz": "Asia/Jakarta",
                    "uid": 2,
                    "allowed_company_ids": [
                        4,
                        2,
                        3
                    ],
                    "default_move_type": "out_invoice",
                    "bin_size": True
                }
            },
            "id": 512700479
        }
        self.client.post("/web/dataset/search_read?move=invoice",
                         headers=pheaders,
                         json=invoice_body
                         )

    @task
    def searchReadBillOdooUI(self):
        bill_body = {
            "jsonrpc": "2.0",
            "method": "call",
            "params": {
                "model": "account.move",
                "domain": [
                    [
                        "move_type",
                        "=",
                        "in_invoice"
                    ]
                ],
                "fields": [
                    "name",
                    "create_uid",
                    "partner_id",
                    "invoice_source_email",
                    "invoice_partner_display_name",
                    "invoice_date",
                    "invoice_date_due",
                    "date",
                    "invoice_origin",
                    "payment_reference",
                    "ref",
                    "invoice_user_id",
                    "l10n_id_tax_number",
                    "l10n_id_csv_created",
                    "team_id",
                    "activity_ids",
                    "activity_exception_decoration",
                    "activity_exception_icon",
                    "activity_state",
                    "activity_summary",
                    "activity_type_id",
                    "activity_type_icon",
                    "company_id",
                    "amount_untaxed_signed",
                    "amount_tax_signed",
                    "amount_total_signed",
                    "amount_residual_signed",
                    "currency_id",
                    "company_currency_id",
                    "state",
                    "ar_customer_status",
                    "invoice_payment_method",
                    "posted_date",
                    "register_payment_date",
                    "is_generate",
                    "payment_state",
                    "move_type"
                ],
                "limit": 20,
                "sort": "",
                "context": {
                    "lang": "en_US",
                    "tz": "Asia/Jakarta",
                    "uid": 2,
                    "allowed_company_ids": [
                        4,
                        2,
                        3
                    ],
                    "default_move_type": "in_invoice",
                    "bin_size": True
                }
            },
            "id": 603438751
        }
        self.client.post("/web/dataset/search_read?move=bill",
                         headers=pheaders,
                         json=bill_body
                         )

    @task
    def restAPIOdoo5(self):
        self.client.get("/",
                        headers=pheaders
                        )

    @task
    def restAPIOdoo6(self):
        self.client.get("/web",
                        headers=pheaders
                        )

