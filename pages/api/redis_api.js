import { createClient } from "redis"


console.log(process.env.NAME)
const client = createClient({
  socket: {
    port: 12332,
    host: process.env.ENDPOINT
  },
  password: process.env.PASSWORD

})

export default async function handler(req, res) {
  let value = JSON.parse(req.body).usrInp
  let obj = {}

  await client.connect()

  try {
    for await (let k of client.scanIterator()) {
      if (value == k) {
        obj = {
          response: await client.get(k),
          new_key: false
        }
        res.json(obj)

        await client.del(k)
        await client.quit()
        return
      }
    }

    let randomKey = Math.floor(100000 + Math.random() * 900000)
    await client.set(randomKey.toString(), value)
    obj = {
      response: randomKey,
      new_key: true

    }

    res.json(obj)

    await client.quit()

    setTimeout(async () => {

      await client.connect()
      await client.del(randomKey.toString())
      await client.quit()
      console.log("Key Deleted")

    }, 100000)


  } catch (e) {
    console.error(e)
  }
}
