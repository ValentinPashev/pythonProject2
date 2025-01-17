from project import BaseCampaign


class LowBudgetCampaign(BaseCampaign):

    def __init__(self, campaign_id: int, brand: str, required_engagement: float):
        super().__init__(campaign_id, brand, 2500.0, required_engagement)

    def check_eligibility(self, engagement_rate: float) -> bool:
        return engagement_rate >= 0.9 * self.required_engagement
