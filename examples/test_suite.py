from resttest import request, response, case, suite

test_case_1 = test_case(
    context={
        'subject': 'test',
        'fsdf': 'fsdf',
        'user': random_subsriber,
        },
    depends_on=[],

    request=request(
        uri='/appmail/messages',
        method='POST',
        authentication=['%(user)s', '%(password)s'],
        headers={'Content-Type': ''},
        body="""<?xml version="1.0" encoding="utf-8"?>
                <entry>
                <link rel="report" href="http://59.108.16.185:7790/humana/report"/>
                <trackingId>%s</trackingId>

                <subject><![CDATA[%(subject)s]]></subject>
                <body><![CDATA[%(body)s]]></body>
                <secure>%(subject)s</secure>

                <expire>
                    <aliveDuration>%s</aliveDuration>
                </expire>

                <pushNotification>
                    <subject><![CDATA[%s]]></subject>
                    <sound>Sound name</sound>
                    <params>
                        <param>
                            <key>key-tet</key>
                            <value>value string</value>
                        </param>
                    </params>
                </pushNotification>

                %s
                %s
            </entry>

            """
    ),
    response=response(
        status=123,
        body="""
            <entry><title>%(title)s</title></entry>
            """
    ),

    follow_verification = callback,

    )

suite1 = suite(
    context={
        'user':'ff'
    },
    prepare=[

    ],
    tests=[
            test_case_1,

    ]
)