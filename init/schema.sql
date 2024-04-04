CREATE TABLE "events" (
	"id" TEXT not null primary key,
	"title" text not null,
	"details" text,
	"slug" text not null,
	"maximum_attendees" integer
);

CREATE TABLE "attendees" (
	"id" text not null primary key,
	"name" text not null,
	"email" text not null,
	"event_id" text not null,
	"created_at" datetime not null default current_timestamp,
	constraint "attendees_event_id_fkey" foreign key ("event_id") references "events" ("id") on delete restrict on update cascade
);

CREATE TABLE "check_ins" (
	"id" integer not null primary key autoincrement,
	"created_at" datetime not null default current_timestamp,
	"attendeeId" text not null,
	constraint "check_ins_attendeeId_fkey" foreign key ("attendeeId") references "attendees" ("id") on delete restrict on update cascade
);

create unique index "events slug key" on "events"("slug");
create unique index "attendees_event_id_email_key" on "attendees"("event_id", "email");
create unique index "check_ins_attendeeId_key" on "check_ins"("attendeeId");