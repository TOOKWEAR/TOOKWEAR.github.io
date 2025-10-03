import express from "express";
import { status } from "minecraft-server-util";
import path from "path";
import { fileURLToPath } from "url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
const PORT = process.env.PORT || 3000;

// Static Files (Website)
app.use(express.static(path.join(__dirname, "public")));

// API Endpoint
app.get("/api/status", async (req, res) => {
  try {
    const data = await status("dein.server.ip", 25565);
    res.json({
      online: true,
      players: data.players.online,
      max: data.players.max,
      version: data.version.name,
    });
  } catch (err) {
    res.json({ online: false });
  }
});

app.listen(PORT, () => console.log(`Took-Wear läuft auf http://localhost:${PORT}`));