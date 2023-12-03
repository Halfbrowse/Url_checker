import sqlite3


def create_database():
    conn = sqlite3.connect("admin_panel.db")
    c = conn.cursor()

    c.execute(
        """
        CREATE TABLE IF NOT EXISTS Entities (
            id INTEGER PRIMARY KEY,
            Name TEXT,
            Alias TEXT,
            Type TEXT,
            Attribution TEXT,
            Attribution_links TEXT,
            Attribution_type TEXT,
            Attribution_confidence INTEGER,
            Label TEXT,
            Parent_actor TEXT,
            Subsidiary_actors TEXT,
            Threat_Actor TEXT,
            TTPs TEXT,
            Description_of_TTPs TEXT,
            Description_TTPs_Link TEXT,
            Master_Narratives TEXT,
            Master_Narrative_Description TEXT,
            Master_Narrative_Links TEXT,
            Summary TEXT,
            External_links TEXT,
            Language TEXT,
            Country TEXT,
            Sub_region TEXT,
            Region TEXT,
            Website TEXT,
            Twitter TEXT,
            Twitter_ID TEXT,
            Facebook TEXT,
            Threads TEXT,
            YouTube TEXT,
            YouTube_ID TEXT,
            TikTok TEXT,
            Instagram TEXT,
            LinkedIn TEXT,
            Reddit TEXT,
            VK TEXT,
            Telegram TEXT,
            Substack TEXT,
            Quora TEXT,
            Patreon TEXT,
            GoFundMe TEXT,
            Paypal TEXT,
            Twitch TEXT,
            Mastadon TEXT,
            Wechat TEXT,
            QQ TEXT,
            Douyin TEXT
        )
    """
    )

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_database()
