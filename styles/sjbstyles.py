from mailman.core.i18n import _
from mailman.interfaces.action import Action
from mailman.interfaces.mailinglist import (ReplyToMunging, SubscriptionPolicy)
from mailman.interfaces.styles import IStyle
from mailman.styles.base import (
    Announcement, BasicOperation, Bounces, Discussion, Identity, Moderation,
    Public)
from public import public
from zope.interface import implementer

@public
@implementer(IStyle)
class SJBDefaultStyle(Identity, BasicOperation, Bounces, Public, Discussion, Moderation):

    name = 'sjb-list-style'

    def apply(self, mailing_list):
        Identity.apply(self, mailing_list)
        BasicOperation.apply(self, mailing_list)
        Bounces.apply(self, mailing_list)
        Public.apply(self, mailing_list)
        Discussion.apply(self, mailing_list)
        Moderation.apply(self, mailing_list)
        # these set the basic things right. We change the rest at the end
        self.applySjbRules(mailing_list)

    def applySjbRules(self, mailing_list):
        mlist = mailing_list
        mlist.display_name = mlist.list_name
        mlist.subject_prefix = _('[$mlist.list_name] ') # _() calls gettext, which is supposedly useful
        mlist.reply_to_address = mlist.list_name + '@' + mlist.mail_host # which is equal to list-address
        mlist.reply_goes_to_list = ReplyToMunging.point_to_list
        mlist.advertised = False # so list doesnt show up when not logged in
        mlist.default_member_action = Action.accept # member posts are accepted immediately
        mlist.default_nonmember_action = Action.accept # nonmember posts are accepted immediately
        mlist.subscription_policy = SubscriptionPolicy.open # Subscribing members requires no additional checks
        mlist.admin_notify_mchanges = True # Changes to subscriptions are mailed to list admin
