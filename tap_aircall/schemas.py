from singer_sdk.typing import (
    ArrayType,
    BooleanType,
    DateTimeType,
    EmailType,
    IntegerType,
    ObjectType,
    PropertiesList,
    Property,
    StringType,
)

from .typing import OptionalPropertiesList

number_properties = PropertiesList(
    Property(
        "id",
        IntegerType,
        required=True,
        description="Unique identifier for the Number.",
    ),
    Property("direct_link", StringType, description="Direct API URL."),
    Property("name", StringType, description="The name of the Number."),
    Property("digits", StringType, description="International format of the Number."),
    Property(
        "created_at",
        DateTimeType,
        description="Timestamp when the Number was created, in UTC.",
    ),
    Property(
        "country",
        StringType,
        description="ISO 3166-1 alpha-2 country code of the Number.",
    ),
    Property(
        "time_zone", StringType, description="Number's time zone, set in the Dashboard."
    ),
    Property(
        "open",
        BooleanType,
        description="Current opening state of the Number, based on its opening hours.",
    ),
    Property(
        "availability_status",
        StringType,
        description="Current availability status of the Number. open, custom, closed ",
    ),
    Property(
        "is_ivr",
        BooleanType,
        description="true if Number is an IVR, false if Number is a Classic Number.",
    ),
    Property(
        "live_recording_activated",
        BooleanType,
        description="Whether a Number has live recording activated or not.",
    ),
    Property(
        "users",
        ArrayType(
            ObjectType(
                Property(
                    "id", IntegerType, description="Unique identifier for the User."
                ),
                Property("direct_link", StringType, description="Direct API URL."),
                Property(
                    "name",
                    StringType,
                    description="Full name of the User. Results of first_name last_name.",
                ),
                Property("email", StringType, description="Email of the User."),
                Property(
                    "created_at",
                    DateTimeType,
                    description="Timestamp when the User was created, in UTC.",
                ),
                Property(
                    "available",
                    BooleanType,
                    description="Current availability status of the User, based on their working hours.",
                ),
                Property(
                    "availability_status",
                    StringType,
                    description="Current working status of the User. Can be available, custom (= available according to their Working Hours and Timezone) or unavailable (= Do Not Disturb or other unavailable status). More availablility statuses can be retrieved, see the Availability table below.",
                ),
                Property(
                    "time_zone",
                    StringType,
                    description="The User's timezone. This can be set either from the Dashboard or the Phone (check our Knowledge Base). Default is Etc/UTC. More details on Timezones here.",
                ),
                Property(
                    "language",
                    StringType,
                    description="The User's preferred language. This can be set either from the Dashboard or the Phone (check our Knowledge Base). The format is IETF language tag. Default is en-US.",
                ),
                Property(
                    "wrap_up_time",
                    IntegerType,
                    description="A pre-set timer triggered after a call has ended, during which the user can’t receive any calls",
                ),
            )
        ),
        description="List of Users linked to this Number.",
    ),
    Property(
        "priority",
        IntegerType,
        description="Priority level of the number used during routing of the calls. Can be null, 0 (no priority) or 1 (top priority). Default value is null ",
    ),
    Property(
        "messages",
        ObjectType(
            Property(
                "welcome",
                StringType,
                description="Welcome message URL. This file is played at the beginning of an incoming call.",
            ),
            Property(
                "waiting",
                StringType,
                description="Waiting music URL. Caller will hear this if they are put on hold during an ongoing call or while the call is being transfered.",
            ),
            Property(
                "ringing_tone",
                StringType,
                description="Ringing tone URL. During an incoming call, caller will hear this music while waiting for the call to be answered.",
            ),
            Property(
                "unanswered_call",
                StringType,
                description="Unanswered Call message URL. Caller will hear this message if their call is not answered when the business hours are open.",
            ),
            Property(
                "after_hours",
                StringType,
                description="After Hours message URL. Caller will hear this message if they call outside of this number's business hours.",
            ),
            Property(
                "ivr",
                StringType,
                description="IVR message URL. Caller will hear this right after the Welcome message. This message will be played twice.",
            ),
            Property(
                "voicemail",
                StringType,
                description="Voicemail message URL. Deprecated: replaced by unanswered_call.",
            ),
            Property(
                "closed",
                StringType,
                description="Closed message URL. Deprecated: replaced by after_hours.",
            ),
            Property(
                "callback_later", StringType, description="Callback Later message."
            ),
        ),
        description="URL to Number's music & messages files.",
    ),
)

user_properties = PropertiesList(
    Property(
        "id", IntegerType, required=True, description="Unique identifier for the User."
    ),
    Property("direct_link", StringType, description="Direct API URL."),
    Property(
        "name",
        StringType,
        description="Full name of the User. Results of first_name last_name.",
    ),
    Property("email", EmailType, description="Email of the User."),
    Property(
        "created_at",
        DateTimeType,
        description="Timestamp when the User was created, in UTC.",
    ),
    Property(
        "available",
        BooleanType,
        description="Current availability status of the User, based on their working hours.",
    ),
    Property(
        "availability_status",
        StringType,
        description="Current working status of the User. Can be available, custom (= available according to their Working Hours and Timezone) or unavailable (= Do Not Disturb or other unavailable status). More availablility statuses can be retrieved, see the Availability table below.",
    ),
    Property(
        "numbers",
        ArrayType(number_properties),
        description="List of Numbers associated to this User.",
    ),
    Property(
        "time_zone",
        StringType,
        description="The User's timezone. This can be set either from the Dashboard or the Phone (check our Knowledge Base). Default is Etc/UTC. More details on Timezones here.",
    ),
    Property(
        "language",
        StringType,
        description="The User's preferred language. This can be set either from the Dashboard or the Phone (check our Knowledge Base). The format is IETF language tag. Default is en-US.",
    ),
    Property(
        "wrap_up_time",
        IntegerType,
        description="A pre-set timer triggered after a call has ended, during which the user can’t receive any calls",
    ),
)

availability_properties = PropertiesList(
    Property("available", StringType, description="Agent ready to answer calls."),
    Property("offline", StringType, description="Agent not online."),
    Property(
        "do_not_disturb",
        StringType,
        description="Agent toggled themself as do not disturb.",
    ),
    Property("in_call", StringType, description="Agent is currently on a call."),
    Property(
        "after_call_work",
        StringType,
        description="Agent is performing their after-call work (tagging a call or wrapping up).",
    ),
)

# From https://developer.aircall.io/api-references/#team-overview
teams_properties = OptionalPropertiesList(
    Property(
        "id", IntegerType, required=True, description="Unique identifier for the Team."
    ),
    Property("direct_link", StringType, description="Direct API URL."),
    Property(
        "name",
        StringType,
        description="Full name of the Team. name must be unique in a company and the length of the string should 64 characters maximum.",
    ),
    Property(
        "created_at",
        DateTimeType,
        description="Timestamp when the Team was created, in UTC.",
    ),
    Property(
        "users",
        ArrayType(user_properties),
        description="List of Users associated to this Team.",
    ),
)

contact_properties = PropertiesList(
    Property(
        "id",
        IntegerType,
        required=True,
        description="Unique identifier for the Contact.",
    ),
    Property("direct_link", StringType, description="Direct API URL."),
    Property("first_name", StringType, description="Contact's first name."),
    Property("last_name", StringType, description="Contact's last name."),
    Property("company_name", StringType, description="Contact's company name."),
    Property(
        "description", StringType, description="Field used by Aircall to qualify tags."
    ),
    Property(
        "information", StringType, description="Extra information about the contact."
    ),
    Property(
        "is_shared",
        BooleanType,
        description="Contact can be shared within the organization.",
    ),
    Property(
        "created_at",
        DateTimeType,
        description="Timestamp when the Contact was created, in UTC.",
    ),
    Property(
        "updated_at",
        DateTimeType,
        description="Timestamp when the Contact was updated, in UTC.",
    ),
    Property(
        "phone_numbers",
        ArrayType(
            ObjectType(
                Property(
                    "id",
                    IntegerType,
                    description="Unique identifier for this phone number.",
                ),
                Property(
                    "label", StringType, description="A custom label like work, home..."
                ),
                Property("value", StringType, description="The raw phone number."),
            )
        ),
        description="Phone numbers of this contact.",
    ),
    Property(
        "emails",
        ArrayType(
            ObjectType(
                Property(
                    "id",
                    IntegerType,
                    description="Unique identifier for this email address.",
                ),
                Property(
                    "label", StringType, description="A custom label like work, home..."
                ),
                Property("value", StringType, description="The email address."),
            )
        ),
        description="Email addresses of this contact.",
    ),
)

tag_properties = PropertiesList(
    Property(
        "id", IntegerType, required=True, description="Unique identifier for the Tag."
    ),
    Property("direct_link", StringType, description="Direct API URL."),
    Property("name", StringType, description="Tag's name."),
    Property(
        "color",
        StringType,
        description="The color that this tag is displayed in. In Hexadecimal format.",
    ),
    Property(
        "description", StringType, description="Field used by Aircall to qualify Tags."
    ),
)

call_properties = PropertiesList(
    Property(
        "id", IntegerType, required=True, description="Unique identifier for the Call."
    ),
    Property("direct_link", StringType, description="Direct API URL."),
    Property(
        "started_at",
        DateTimeType,
        description="Timestamp when the Call started, in UTC.",
    ),
    Property(
        "answered_at",
        DateTimeType,
        description="Timestamp when the Call has been answered, in UTC.",
    ),
    Property(
        "ended_at", DateTimeType, description="Timestamp when the Call ended, in UTC."
    ),
    Property(
        "duration",
        IntegerType,
        description="Duration of the Call in seconds. This field is computed by started_at - ended_at.",
    ),
    Property(
        "status",
        StringType,
        description="Current status of the Call. Can be initial, answered or done.",
    ),
    Property(
        "direction",
        StringType,
        description="Direction of the Call. Could be inbound or outbound.",
    ),
    Property(
        "raw_digits",
        StringType,
        description="International format of the number of the caller or the callee. For an anonymous call, the value is anonymous.",
    ),
    Property(
        "asset",
        StringType,
        description="If present, a secured webpage containing the voicemail or live recording for this Call. URL format is https://assets.aircall.io/[recording,voicemail]/:call_id.",
    ),
    Property(
        "recording",
        StringType,
        description="If present, the direct URL of the live recording (mp3 file) for this Call. This feature can be enabled from the Aircall Dashboard, on each Number - more information in our Knowledge Base. This link is valid for 10min. only.",
    ),
    Property(
        "voicemail",
        StringType,
        description="Only present if a voicemail was left. Voicemails can only be left by callers on inbound calls. If present, the direct URL of a voicemail (mp3 file) for this Call. This link is valid for 10min. only.",
    ),
    Property("archived", BooleanType, description="Describe if Call needs follow up."),
    Property(
        "missed_call_reason",
        BooleanType,
        description="Representing the reason why the Call was missed. Can be out_of_opening_hours, short_abandoned, abandoned_in_ivr, abandoned_in_classic, no_available_agent or agents_did_not_answer.",
    ),
    Property("cost", StringType, description="Cost of the Call in U.S. cents."),
    Property(
        "number",
        number_properties,
        description="Full Number object attached to the Call.",
    ),
    Property(
        "user",
        user_properties,
        description="Full User object who took or made the Call.",
    ),
    Property(
        "contact",
        contact_properties,
        description="Full Contact object attached to the Call.",
    ),
    Property(
        "assigned_to",
        user_properties,
        description="Full User object assigned to the Call.",
    ),
    Property(
        "teams",
        ArrayType(teams_properties),
        description="Full Teams object assigned to the Call. Teams are only assigned to inbound calls.",
    ),
    Property(
        "transferred_by",
        user_properties,
        description="User who performed the Call transfer.",
    ),
    Property(
        "transferred_to",
        user_properties,
        description="User to whom the Call was transferred to.",
    ),
    Property(
        "comments",
        ArrayType(
            ObjectType(
                Property(
                    "id", IntegerType, description="Unique identifier for the Comment."
                ),
                Property(
                    "content",
                    StringType,
                    description="Content of the Comment, written by Agent or via Public API.",
                ),
                Property(
                    "posted_at",
                    IntegerType,
                    description="UNIX timestamp when the Comment was created, in UTC.",
                ),
                Property(
                    "posted_by",
                    user_properties,
                    description="User object who created the Comment.",
                ),
            )
        ),
    ),
    Property(
        "tags",
        ArrayType(tag_properties),
        description="Tags added to this Call by Users.",
    ),
    Property(
        "participants",
        ArrayType(
            ObjectType(
                Property(
                    "id",
                    StringType,
                    description="Either Contact or User id. Not present for external",
                ),
                Property(
                    "type",
                    StringType,
                    description="It will be 'user', 'contact' or 'external'",
                ),
                Property(
                    "name",
                    StringType,
                    description="Participant's full name. Not present for external",
                ),
                Property(
                    "phone_number",
                    StringType,
                    description="Not present in a user type participant",
                ),
            )
        ),
        description="Participants involved in a conference call.",
    ),
)
