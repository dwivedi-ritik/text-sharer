// Next.js API route support: https://nextjs.org/docs/api-routes/introduction
import { createClient } from "redis"

const client = createClient({
  socket: {
    port: 12332,
    host: "redis-12332.c212.ap-south-1-1.ec2.cloud.redislabs.com"
  },
  password: 'DKpPS8NXpH3IVZCphq2m2GVooXtjJASQ'

})

export default async function handler(req, res) {
  let value = JSON.parse(req.body).usrInp
  let obj = {}
  await client.connect()

  try {
    for await (let k of client.scanIterator()) {
      if (value == k) {
        obj["response"] = await client.get(k)
        await client.del(k)
        await client.quit()
        res.json(obj)
        return
      }
    }

    let randomKey = Math.floor(100000 + Math.random() * 900000)
    await client.set(randomKey.toString(), value)
    obj["response"] = randomKey
    res.json(obj)

    await client.quit()

  } catch (e) {
    console.error(e)
  }
  // res.status(200).json({ name: 'John Doe' })
}
