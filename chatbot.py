def get_response(message):
    message = message.lower()

    try:
        if "days=" in message and "hours=" in message:

            parts = message.split(";")

            # Extract days and hours
            days = int(parts[0].split("=")[1])
            hours = int(parts[1].split("=")[1])

            subjects = {}

            # Extract subjects and topics
            for part in parts[2:]:
                if ":" in part:
                    name, topics = part.split(":")
                    topics_list = topics.split(",")
                    subjects[name.strip()] = [t.strip() for t in topics_list]

            # Combine all topics
            all_topics = []

            for sub, topics in subjects.items():
                for topic in topics:
                    all_topics.append((sub, topic))

            if not all_topics:
                return "Please enter subjects and topics."

            timetable = ""
            total_topics = len(all_topics)

            topics_per_day = max(1, (total_topics + days - 1) // days)

            index = 0

            for d in range(days):
                timetable += f"\n📅 Day {d+1}:\n"

                count = 0

                while count < topics_per_day and index < total_topics:
                    sub, topic = all_topics[index]

                    timetable += f"  • {sub.upper()} → {topic} ({hours // topics_per_day} hrs)\n"

                    index += 1
                    count += 1

            timetable += "\n✅ Stay consistent and revise daily!"

            return timetable

        else:
            return (
                "Use format:\n"
                "days=5; hours=6; OS:process,threads; CN:osi,tcp"
            )

    except:
        return "⚠ Invalid format. Please try again."
