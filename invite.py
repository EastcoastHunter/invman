# Invite Manager Bot written in discord.py

import discord
client=discord.Client()

@client.event
async def on_ready():
    global role_list
    print('Logged in as: '+client.user.name)
    print('Bot ID: '+client.user.id)
    await client.change_presence(game=discord.Game(name=',invite - lists your invites'))
    print('------\n')
    for server in client.servers:
        role_list=dict((role.name,role) for role in server.roles)

@client.event
async def on_member_join(new_member):
    invites=await client.invites_from(new_member.sever)
    for member in new_member.server.members: 
        if member.bot==False:
            use=0
            prole=None
            for invite in invites:
                if invite.max_age==0 and invite.inviter==member:
                    uses += invite.uses

            for role,used in role_ranks.items():
                if uses in used and role_list[role] not in member.roles:
                    for mrole in member.role:
                        if mrole.name in role_ranks.key():
                            await client.remove_roles(member,mrole)
                        await client.send_message(member, "Congratulations {}, you have been promoted to **{}**!".format(member.mention,role))
                        await client.add_role(member,role_list[role])

@client.event
async def on_message(message):
    if message.content==',invites':
        total_uses=0
        embed=discord.Embed(title='__Invites from {}__'.format(message.author.name))
        invites = await client.invites_from(message.server)
        for invite in invites:
            if invite.inviter == message.author and invite.max_age=0:
                total_uses += invite.uses
                embed.add_field(name='Invite',value=invite.id)
                embed.add_field(name='Uses', value=invite.uses)
                embed.add_field(name='Expires', value='Never')
            embed.add_field(name='__Total Uses__',value=total_uses)
            await client.send_message(message.channel,embed=embed)

client.run(process.env.token)